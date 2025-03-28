package br.edu.ibmec.cloud.ecommerce_cloud.configuration;

import org.springframework.boot.context.properties.ConfigurationProperties;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@ConfigurationProperties(prefix = "azure.cosmos")
public class CosmosProperties {

    private String uri;

    private String key;

    private String database;

    private boolean queryMetricsEnabled;

    private boolean responseDiagnosticsEnabled;

}
