package br.edu.ibmec.cloud.ecommerce_cloud.controller;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RequestMapping("/users")
@RestController
public class UserController {

    @GetMapping
    public ResponseEntity<String> getUser() {
        return new ResponseEntity<>("Hello World API Java", HttpStatus.OK);
    }

}
