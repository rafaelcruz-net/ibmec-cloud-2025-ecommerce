package br.edu.ibmec.cloud.ecommerce_cloud.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import br.edu.ibmec.cloud.ecommerce_cloud.model.User;
import br.edu.ibmec.cloud.ecommerce_cloud.repository.UserRepository;

@RequestMapping("/users")
@RestController
public class UserController {

    @Autowired
    private UserRepository userRepository;

    @GetMapping
    public ResponseEntity<User> getUser() {
        User response = userRepository.findById(1).get();
        return new ResponseEntity<>(response, HttpStatus.OK);
    }

}
