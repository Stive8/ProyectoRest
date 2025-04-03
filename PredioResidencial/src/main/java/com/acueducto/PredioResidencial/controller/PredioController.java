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
    public ResponseEntity<HttpStatus> crearPredio(@RequestBody Request request) {

        System.out.println("Peticion POST");

        try {
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

            return new ResponseEntity<>(HttpStatus.OK);
        } catch (Exception e) {
            return new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
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

    /*
    @GetMapping(value = "/")
    public Integer getValue() {
        return value;
    }
    */

//    @GetMapping(value = "/test")
//    public ResponseEntity<Employee> getValue() {
//        //Employee emp = new Employee(123, "Pedro");
//        if (emp != null) {
//            return ResponseEntity.ok(emp);
//        }
//        System.out.println("ME TOCARON");
//        return ResponseEntity.notFound().build();
//    }
//
//
//    @PostMapping(value = "/{value}")
//    public void setValue(@PathVariable("value") Integer value) {
//        System.out.println("Value = " + value);
//        this.value = value;
//    }

    /*
    @PostMapping(value = "/set")
    public void setValue2(@RequestParam("value") Optional<Integer> value) {
        if (value.isPresent()) {
            System.out.println("Value = " + value);
            this.value = value.get();
        } else {
            System.out.println("NO ESTA!");
        }
    }
     */

//    @PostMapping(value = "/set")
//    public Employee setValue2(@RequestBody Employee emp) {
//
//        this.emp = emp;
//
//        return emp;
//    }
}
