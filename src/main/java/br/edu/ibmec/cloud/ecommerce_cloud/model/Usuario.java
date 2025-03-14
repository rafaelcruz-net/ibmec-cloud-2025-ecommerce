package br.edu.ibmec.cloud.ecommerce_cloud.model;

import java.time.LocalDateTime;
import java.util.List;

import jakarta.persistence.*;
import lombok.Data;

@Data
@Entity(name = "usuario")
public class Usuario {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;
    
    @Column
    private String nome;

    @Column
    private LocalDateTime dtNascimento;

    @Column
    private String cpf;

    @Column
    private String email;

    @OneToMany
    @JoinColumn(referencedColumnName = "id", name = "id_usuario")
    private List<Cartao> cartoes;

    @OneToMany
    @JoinColumn(referencedColumnName = "id", name = "id_usuario")
    private List<Endereco> enderecos;
}
