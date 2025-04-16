package br.edu.ibmec.cloud.ecommerce_cloud.controller;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.HttpStatusCode;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

import br.edu.ibmec.cloud.ecommerce_cloud.model.Product;
import br.edu.ibmec.cloud.ecommerce_cloud.repository.cosmos.ProductRepository;


@RestController
@RequestMapping("/products")
public class ProductController {

    @Autowired
    private ProductRepository repository;

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public ResponseEntity<Product> create(@RequestBody Product product) {
        
        //Gerando identificadores unicos
        product.setId(UUID.randomUUID().toString());
        repository.save(product);

        return new ResponseEntity<>(product, HttpStatus.CREATED);
    }

    @GetMapping("{id}")
    public ResponseEntity<Product> get(@PathVariable String id) {
        Optional<Product> optProduct = this.repository.findById(id);

        if (optProduct.isEmpty()) {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }

        return new ResponseEntity<>(optProduct.get(), HttpStatus.OK);
    }

    @GetMapping()
    public ResponseEntity<Iterable<Product>> getAll() {
        List<Product> result = new ArrayList<>();
        repository.findAll().forEach(result::add);
        return new ResponseEntity<>(result, HttpStatus.OK);
    }


    @DeleteMapping("{id}")
    public ResponseEntity<Product> delete(@PathVariable String id) {
        Optional<Product> optProduct = this.repository.findById(id);

        if (optProduct.isEmpty()) {
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }

        this.repository.delete(optProduct.get());
        return new ResponseEntity<>(HttpStatus.NO_CONTENT);
    }




}
