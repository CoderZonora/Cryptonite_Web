package com.example.CRUD;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication //This single annotation is equivalent to using @Configuration, @EnableAutoConfiguration, and @ComponentScan.
public class CrudBasicApplication {

	public static void main(String[] args) {
		SpringApplication.run(CrudBasicApplication.class, args);
	}

}
