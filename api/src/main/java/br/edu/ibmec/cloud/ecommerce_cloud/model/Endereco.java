package br.edu.ibmec.cloud.ecommerce_cloud.model;

import jakarta.persistence.*;
import lombok.Data;

@Data
@Entity(name = "endereco")
public class Endereco {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @Column
    private String logradouro;

    @Column
    private String complemento;

    @Column
    private String bairro;

    @Column
    private String cidade;

    @Column
    private String estado;

    @Column
    private String cep;
}
