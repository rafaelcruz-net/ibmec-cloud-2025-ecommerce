package br.edu.ibmec.cloud.ecommerce_cloud.model;

import java.time.LocalDateTime;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import lombok.Data;

@Data
@Entity(name = "usuario")
public class User {
    @Id
    private Integer id;
    
    @Column
    private String nome;

    @Column(name = "dt_nascimento")
    private LocalDateTime dtNascimento;

    @Column
    private String cpf;

    @Column
    private String email;
}
