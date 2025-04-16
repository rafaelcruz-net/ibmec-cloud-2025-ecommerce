package br.edu.ibmec.cloud.ecommerce_cloud.repository;

import br.edu.ibmec.cloud.ecommerce_cloud.model.Endereco;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface EnderecoRepository extends JpaRepository<Endereco, Integer> {
}
