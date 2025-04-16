package br.edu.ibmec.cloud.ecommerce_cloud.controller;

import br.edu.ibmec.cloud.ecommerce_cloud.model.Cartao;
import br.edu.ibmec.cloud.ecommerce_cloud.model.Usuario;
import br.edu.ibmec.cloud.ecommerce_cloud.repository.CartaoRepository;
import br.edu.ibmec.cloud.ecommerce_cloud.repository.UsuarioRepository;
import br.edu.ibmec.cloud.ecommerce_cloud.request.TransacaoRequest;
import br.edu.ibmec.cloud.ecommerce_cloud.request.TransacaoResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.time.LocalDateTime;
import java.util.Optional;
import java.util.UUID;

@RestController
@RequestMapping("/credit_card/{id_user}")
public class CartaoController {

    @Autowired
    private CartaoRepository cartaoRepository;

    @Autowired
    private UsuarioRepository usuarioRepository;

    @PostMapping
    public ResponseEntity<Cartao> create(@PathVariable("id_user") int id_user, @RequestBody Cartao cartao) {
        //Verificando se o usuario existe na base
        Optional<Usuario> optionalUsuario = this.usuarioRepository.findById(id_user);

        if (optionalUsuario.isEmpty())
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);

        //Cria o cartao de credito na base
        cartaoRepository.save(cartao);

        //Associa o cartao de credito ao usuario
        Usuario usuario = optionalUsuario.get();

        usuario.getCartoes().add(cartao);
        usuarioRepository.save(usuario);

        return new ResponseEntity<>(cartao, HttpStatus.CREATED);

    }

    @PostMapping("/authorize")
    public ResponseEntity<TransacaoResponse> authorize(@PathVariable("id_user") int id_user, @RequestBody TransacaoRequest request) {
        //Verificando se o usuario existe na base
        Optional<Usuario> optionalUsuario = this.usuarioRepository.findById(id_user);

        if (optionalUsuario.isEmpty())
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);

        Usuario usuario = optionalUsuario.get();
        Cartao cartaoCompra = null;

        //Busca os dados do cartao de credito;
        for (Cartao cartao: usuario.getCartoes()) {
            if (request.getNumero().equals(cartao.getNumero()) && request.getCvv().equals(cartao.getCvv())) {
                cartaoCompra = cartao;
                break;
            }
        }

        //Não achei o cartao do usuario
        if (cartaoCompra == null) {
            TransacaoResponse response = new TransacaoResponse();
            response.setStatus("NOT_AUTHORIZED");
            response.setDtTransacao(LocalDateTime.now());
            response.setMessage("Cartão não encontrado para o usuario");
            return new ResponseEntity<>(response, HttpStatus.NOT_FOUND);
        }


        //Verifica se o cartao não está expirado
        if (cartaoCompra.getDtExpiracao().isBefore(LocalDateTime.now())) {
            TransacaoResponse response = new TransacaoResponse();
            response.setStatus("NOT_AUTHORIZED");
            response.setDtTransacao(LocalDateTime.now());
            response.setMessage("Cartão Expirado");
            return new ResponseEntity<>(response, HttpStatus.BAD_REQUEST);
        }

        //Verifica se tem dinheiro no cartao para realizr a compra
        if (cartaoCompra.getSaldo() < request.getValor()) {
            TransacaoResponse response = new TransacaoResponse();
            response.setStatus("NOT_AUTHORIZED");
            response.setDtTransacao(LocalDateTime.now());
            response.setMessage("Sem saldo para realizar a compra");
            return new ResponseEntity<>(response, HttpStatus.BAD_REQUEST);
        }

        //Debita no cartao de credito o valor da compra
        cartaoCompra.setSaldo(cartaoCompra.getSaldo() - request.getValor());

        //Atualiza o cartao na base de dados
        cartaoRepository.save(cartaoCompra);

        TransacaoResponse response = new TransacaoResponse();
        response.setStatus("AUTHORIZED");
        response.setDtTransacao(LocalDateTime.now());
        response.setMessage("Compra autorizada");
        response.setCodigoAutorizacao(UUID.randomUUID());

        return new ResponseEntity<>(response, HttpStatus.OK);

    }


}
