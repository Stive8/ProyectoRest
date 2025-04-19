package com.acueducto.PredioResidencial.controller;

import com.acueducto.PredioResidencial.model.ActualizarComercialRequest;
import com.acueducto.PredioResidencial.model.Comercial;
import com.acueducto.PredioResidencial.model.Request;
import com.acueducto.PredioResidencial.service.IServicio;
import lombok.AllArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@AllArgsConstructor
@RestController
@RequestMapping(value = "predio")
public class PredioController {

    private final IServicio servicio;

    @PostMapping("crear")
    public ResponseEntity<String> crearPredio(@RequestBody Request request) {

        System.out.println("Petición POST recibida");

        try {
            /*
            // Validación de campos obligatorios
            if (request.getPropietario() == null || request.getPropietario().trim().isEmpty() ||
                    request.getDireccion() == null || request.getDireccion().trim().isEmpty() ||
                    request.getEstrato() < 0 || request.getEstrato() > 6 ||
                    request.getConsumo() < 0 || request.getConsumo() == null) {
                return new ResponseEntity<>("Datos incompletos en la solicitud", HttpStatus.BAD_REQUEST);
            }

            // Validación de fecha de registro
            if (request.getFechaRegistro() == null) {
                return new ResponseEntity<>("La fecha de registro no puede estar vacía", HttpStatus.BAD_REQUEST);
            }

            // Validación de números positivos
            if (request.getEstrato() < 0 || request.getConsumo() < 0 || request.getSubsidio() < 0) {
                return new ResponseEntity<>("Valores numéricos no pueden ser negativos", HttpStatus.BAD_REQUEST);
            } */
            Comercial comercial = servicio.crearPredioComercial(
                    request.getPropietario(),
                    request.getDireccion(),
                    request.getFechaRegistro(),
                    request.getEstrato(),
                    request.getConsumo(),
                    request.getTipoComercio()
            );

            servicio.agregarComercial(comercial);

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

            var predio = servicio.buscarPredioComercialPorId(value);

            if (predio == null) {
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
            var predio = servicio.buscarPredioComercialPorId(value);

            if (predio == null) {
                return ResponseEntity.status(HttpStatus.NOT_FOUND).body("El predio con ID " + value + " no existe.");
            }

            servicio.eliminarPredioComercial(value);
            return new ResponseEntity<>("Predio eliminado correctamente", HttpStatus.OK);

        } catch (Exception e) {
            e.printStackTrace();
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Error al eliminar el predio: " + e.getMessage());
        }
    }

    @PutMapping("actualizar")
    public ResponseEntity<?> actualizarPredio(@RequestBody ActualizarComercialRequest request) {

        Optional<Comercial> existenteOpt = servicio.buscarPredioComercialPorId(request.getIndex());

        if (existenteOpt.isEmpty()) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND)
                    .body("El predio con ID " + request.getIndex() + " no existe.");
        }

        try {
            servicio.actualizarPredioComercial(
                    request.getIndex(),
                    request.getPropietario(),
                    request.getDireccion(),
                    request.getEstrato(),
                    request.getConsumo(),
                    request.getTipoComercio(),
                    request.getCodigoLicencia()
            );

            return ResponseEntity.ok("Predio actualizado correctamente");

        } catch (Exception e) {
            e.printStackTrace();
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                    .body("Error al actualizar el predio: " + e.getMessage());
        }
    }




    @GetMapping("listar")
    public ResponseEntity<List<Comercial>> listarResidenciales() {
        System.out.println("Listar Ok");
        try {
            List<Comercial> residenciales = servicio.getPrediosComerciales();
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
