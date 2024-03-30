package com.example.CRUD;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
//import jakarta.persistence.Column; //If you need to set any custom name of the table

@Entity
public class Product {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO) // Auto will automatically implement the best method as per the Database used
    private Long id;

    private String name;
    private String author;

   protected Product()
   {}

   public Product(String name,String author)
   {
    this.name = name;
    this.author = author;
   }


public Long getId()
{
    return id;
}

public String getAuthor()
{
    return author;
}

public String getName()
{
    return name;
}


public void setName(String name) {
    this.name = name;
}

public void setAuthor(String author) {
    this.author = author;
}

@Override
public String toString() {
    return "Product [id=" + id + ", name=" + name + ", author=" + author + "]";
}
// Required for returning Product from readProduct method as String 

}
