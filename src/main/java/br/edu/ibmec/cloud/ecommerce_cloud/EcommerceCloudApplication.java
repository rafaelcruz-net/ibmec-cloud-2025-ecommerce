package br.edu.ibmec.cloud.ecommerce_cloud;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class EcommerceCloudApplication {

	public static void main(String[] args) {
		//Desliga a validação do certificado
		System.setProperty("javax.net.ssl.trustStore", "NULL");
		System.setProperty("javax.net.ssl.trustStoreType", "Windows-ROOT");
		SpringApplication.run(EcommerceCloudApplication.class, args);
	}

}
