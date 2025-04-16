package com.acueducto.PredioResidencial.controller;

import com.acueducto.PredioResidencial.model.Employee;
import com.acueducto.PredioResidencial.model.Request;
import com.acueducto.PredioResidencial.model.Residencial;
import com.acueducto.PredioResidencial.service.IServicio;
import com.acueducto.PredioResidencial.service.Servicio;
import lombok.AllArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@AllArgsConstructor
@RestController
@RequestMapping(value = "predio")
public class PredioController {

    private final IServicio servicio;

    @PostMapping("crear")
    public ResponseEntity<String> crearPredio(@RequestBody Request request) {

        System.out.println("Petición POST recibida");

        try {
            // Validación de campos obligatorios
            if (request.getPropietario() == null || request.getPropietario().trim().isEmpty() ||
                    request.getDireccion() == null || request.getDireccion().trim().isEmpty() ||
                    request.getEstadoCuenta() == null || request.getEstadoCuenta().trim().isEmpty() ||
                    request.getTipoVivienda() == null || request.getTipoVivienda().trim().isEmpty()) {
                return new ResponseEntity<>("Datos incompletos en la solicitud", HttpStatus.BAD_REQUEST);
            }

            // Validación de fecha de registro
            if (request.getFechaRegistro() == null) {
                return new ResponseEntity<>("La fecha de registro no puede estar vacía", HttpStatus.BAD_REQUEST);
            }

            // Validación de números positivos
            if (request.getEstrato() < 0 || request.getConsumo() < 0 || request.getSubsidio() < 0) {
                return new ResponseEntity<>("Valores numéricos no pueden ser negativos", HttpStatus.BAD_REQUEST);
            }

            // Crear el predio residencial
            Residencial residencial = servicio.crearPredioResidencial(
                    request.getPropietario(),
                    request.getDireccion(),
                    request.getFechaRegistro(),
                    request.getEstadoCuenta(),
                    request.getEstrato(),
                    request.getConsumo(),
                    request.getSubsidio(),
                    request.getTipoVivienda()
            );

            System.out.println(request.toString());
            System.out.println(residencial.toString());

            servicio.agregarResidencial(residencial);

            return new ResponseEntity<>("Predio creado correctamente", HttpStatus.OK);

        } catch (NumberFormatException e) {
            return new ResponseEntity<>("Error de formato en los valores numéricos: " + e.getMessage(), HttpStatus.BAD_REQUEST);
        } catch (IllegalArgumentException e) {
            return new ResponseEntity<>("Error en los datos: " + e.getMessage(), HttpStatus.BAD_REQUEST);
        } catch (Exception e) {
            e.printStackTrace();
            return new ResponseEntity<>("Error interno en el servidor: " + e.getMessage(), HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @GetMapping("buscar/{value}")
    public ResponseEntity<?> consultarPredio(@PathVariable("value") Integer value) {
        try {
            System.out.println("Petición GET");

            var predio = servicio.buscarPredioResidencialPorId(value);

            if (predio == null) {
                // Si no existe, se devuelve un 404 Not Found
                return ResponseEntity.status(HttpStatus.NOT_FOUND).body("El predio con ID " + value + " no existe.");
            }

            return new ResponseEntity<>(predio, HttpStatus.OK);
        } catch (Exception e) {
            e.printStackTrace();
            System.out.println("Petición GET con error");
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Error inesperado: " + e.getMessage());
        }
    }


    @DeleteMapping("eliminar/{value}")
    public ResponseEntity<?> eliminarPredio(@PathVariable("value") Integer value) {
        try {
            var predio = servicio.buscarPredioResidencialPorId(value);

            if (predio == null) {
                // Si no existe, se devuelve un 404 Not Found
                return ResponseEntity.status(HttpStatus.NOT_FOUND).body("El predio con ID " + value + " no existe.");
            }

            // Si existe, se elimina
            servicio.eliminarPredioResidencial(value);
            return new ResponseEntity<>(HttpStatus.NO_CONTENT); // 204 No Content

        } catch (Exception e) {
            e.printStackTrace();
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Error al eliminar el predio: " + e.getMessage());
        }
    }

    @PutMapping("actualizar/{id}")
    public ResponseEntity<?> actualizarPredio(@RequestBody Request request) {
        try {
            // Validar existencia del predio
            Residencial existente = servicio.buscarPredioResidencialPorId(request.getId())
                    .orElseThrow(() -> new RuntimeException("El predio con ID " + request.getId() + " no existe."));
            if (existente == null) {
                return ResponseEntity.status(HttpStatus.NOT_FOUND)
                        .body("El predio con ID " + request.getId() + " no existe.");
            }

            // Validaciones de campos
            if (request.getPropietario() == null || request.getPropietario().trim().isEmpty()) {
                return ResponseEntity.badRequest().body("El propietario debe ser un string no vacío.");
            }

            if (request.getDireccion() == null || request.getDireccion().trim().isEmpty()) {
                return ResponseEntity.badRequest().body("La dirección debe ser un string no vacío.");
            }

            String estado = request.getEstadoCuenta();
            if (estado == null || (!estado.equals("AC") && !estado.equals("INAC"))) {
                return ResponseEntity.badRequest().body("El estado de cuenta debe ser 'AC' o 'INAC'.");
            }

            int estrato = request.getEstrato();
            if (estrato < 1 || estrato > 6) {
                return ResponseEntity.badRequest().body("El estrato debe estar entre 1 y 6.");
            }

            double consumo = request.getConsumo();
            if (consumo < 0) {
                return ResponseEntity.badRequest().body("El consumo debe ser un número positivo.");
            }

            int subsidio = request.getSubsidio();
            if (subsidio < 0) {
                return ResponseEntity.badRequest().body("El subsidio debe ser un número positivo.");
            }

            if (request.getTipoVivienda() == null || request.getTipoVivienda().trim().isEmpty()) {
                return ResponseEntity.badRequest().body("El tipo de vivienda debe ser un string no vacío.");
            }

            // Llamada al servicio con todos los datos ya validados
            servicio.actualizarPredioResidencial(
                    request.getId(),
                    request.getSubsidio(),
                    request.getTipoVivienda(),
                    request.getPropietario(),
                    request.getDireccion(),
                    request.getEstadoCuenta(),
                    request.getEstrato(),
                    request.getConsumo()
            );

            return new ResponseEntity<>(HttpStatus.OK);

        } catch (Exception e) {
            e.printStackTrace();
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                    .body("Error al actualizar el predio: " + e.getMessage());
        }
    }

    @GetMapping("listar")
    public ResponseEntity<List<Residencial>> listarResidenciales() {
        System.out.println("Listar Ok");
        try {
            List<Residencial> residenciales = servicio.getPrediosResidenciales();
            System.out.println("Termino de listas");
            return new ResponseEntity<>(residenciales, HttpStatus.OK);

        } catch (Exception e) {
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
        }

    }

    @GetMapping(value = "/healthCheck")
    public String healthCheck() {
        return "Service status Ok!";
    }

}
