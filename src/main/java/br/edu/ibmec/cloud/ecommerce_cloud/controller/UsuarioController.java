package br.edu.ibmec.cloud.ecommerce_cloud.controller;

import br.edu.ibmec.cloud.ecommerce_cloud.model.Cartao;
import br.edu.ibmec.cloud.ecommerce_cloud.model.Endereco;
import br.edu.ibmec.cloud.ecommerce_cloud.repository.CartaoRepository;
import br.edu.ibmec.cloud.ecommerce_cloud.repository.EnderecoRepository;
import org.apache.catalina.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import br.edu.ibmec.cloud.ecommerce_cloud.model.Usuario;
import br.edu.ibmec.cloud.ecommerce_cloud.repository.UsuarioRepository;

import java.util.Optional;

@RequestMapping("/users")
@RestController
public class UsuarioController {

    @Autowired
    private UsuarioRepository userRepository;

    @Autowired
    private EnderecoRepository enderecoRepository;

    @Autowired
    private CartaoRepository cartaoRepository;


    @GetMapping("{id}")
    public ResponseEntity<Usuario> getUser(@PathVariable("id") int id) {
        Optional<Usuario> response = userRepository.findById(id);

        if (response.isEmpty())
            new ResponseEntity<>(HttpStatus.NOT_FOUND);

        return new ResponseEntity<>(response.get(), HttpStatus.OK);
    }

    @PostMapping
    public ResponseEntity<Usuario> create(@RequestBody Usuario user) {
        this.userRepository.save(user);
        return new ResponseEntity<>(user, HttpStatus.CREATED);
    }

    @PostMapping("{id}/address")
    public ResponseEntity<Usuario> associateAddress(@PathVariable("id") int id,
                                                    @RequestBody Endereco endereco) {
        Optional<Usuario> response = userRepository.findById(id);

        if (response.isEmpty())
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);

        //Cria o endereço na base de dados
        this.enderecoRepository.save(endereco);

        //Associa o endereço ao usuario
        Usuario usuario = response.get();
        usuario.getEnderecos().add(endereco);
        this.userRepository.save(usuario);

        return new ResponseEntity<>(usuario, HttpStatus.CREATED);

    }

    @PostMapping("{id}/credit-card")
    public ResponseEntity<Usuario> associateCreditCard(@PathVariable("id") int id,
                                                       @RequestBody Cartao cartao) {
        Optional<Usuario> response = userRepository.findById(id);

        if (response.isEmpty())
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);

        //Cria o cartao na base de dados
        this.cartaoRepository.save(cartao);

        //Associa o cartao ao usuario
        Usuario usuario = response.get();
        usuario.getCartoes().add(cartao);
        this.userRepository.save(usuario);

        return new ResponseEntity<>(usuario, HttpStatus.CREATED);

    }

}
