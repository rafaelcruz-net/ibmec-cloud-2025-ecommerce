package br.edu.ibmec.cloud.ecommerce_cloud.repository.cosmos;

import org.springframework.stereotype.Repository;

import com.azure.spring.data.cosmos.repository.CosmosRepository;

import br.edu.ibmec.cloud.ecommerce_cloud.model.Product;

@Repository
public interface ProductRepository extends CosmosRepository<Product, String> {

}
