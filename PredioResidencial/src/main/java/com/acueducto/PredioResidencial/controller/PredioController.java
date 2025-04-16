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
    public ResponseEntity<HttpStatus> consultarPredio(@PathVariable("value") Integer value) {
        try {
            System.out.println("Peticion GET");
            return new ResponseEntity(servicio.buscarPredioResidencialPorId(value), HttpStatus.OK);
        } catch (Exception e) {
            e.printStackTrace();
            System.out.println("Peticion GET");
            return ResponseEntity.badRequest().build(); // Devuelve un 400 con cuerpo vacío
        }

    }

    @DeleteMapping("eliminar/{value}")
    public ResponseEntity<Residencial> eliminarPredio(@PathVariable("value") Integer value) {

        try {
            servicio.eliminarPredioResidencial(value);
            return new ResponseEntity<>(HttpStatus.NO_CONTENT); // 204 No Content
        } catch (Exception e) {
            e.printStackTrace();
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR); // 500 Internal Server Error
        }

    }

    @PutMapping("actualizar/{value}")
    public ResponseEntity<HttpStatus> actualizarPredio( @RequestBody Request request) {

        try {

            Residencial residencial = servicio.actualizarPredioResidencial(
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
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);

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
