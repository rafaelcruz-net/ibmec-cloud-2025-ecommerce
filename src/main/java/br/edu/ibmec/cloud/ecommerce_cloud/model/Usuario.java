package br.edu.ibmec.cloud.ecommerce_cloud.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import lombok.Data;

import java.time.LocalDateTime;

@Data
@Entity(name = "usuario")
public class Usuario {
    @Id
    private Integer id;

    @Column
    private String nome;

    @Column
    private String email;

    @Column
    private LocalDateTime dtNascimento;

    @Column
    private String cpf;

    @Column
    private String telefone;
}
