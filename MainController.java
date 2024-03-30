package com.example.CRUD;

import java.util.Optional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

//@Controller defined that this class is to be used to handle web requests
@RestController //Specialised version of @Controller used to handle RESTful API like GET,POST etc.
@RequestMapping(path="/demo")
public class MainController {
    @Autowired // This injects the beans of Product_Repository into this class
    private Product_Reposiitory productRepository;

    @PostMapping(path="/add")
    public @ResponseBody String addNewProduct (@RequestParam String name, @RequestParam String author) {
        Product p = new Product(name, author);
        productRepository.save(p);
        return "Saved";
    }

    @GetMapping(path ="read/{id}")
    public @ResponseBody String readProduct(@PathVariable Long id){
        Optional<Product> optionalProduct = productRepository.findById(id); // returns empty instance if entity with given ID not found
    if(optionalProduct.isPresent()) { 
        Product product = optionalProduct.get();
        return product.toString(); // The toString method is Product.java will handle further
    }
    else
    {
        return "Product not found";
    }
    }
    
    @GetMapping(path="/all")
    public @ResponseBody Iterable<Product> getAllProducts() {
        return productRepository.findAll();
    }

    /*
    If need to return as String:

     @GetMapping(path="/all")
public @ResponseBody String getAllProducts() {
    Iterable<Product> products = productRepository.findAll();
    StringBuilder sb = new StringBuilder();
    products.forEach(product -> {
        sb.append(product.toString());
        sb.append("\n");
    });
    return sb.toString();
}
     */

    @DeleteMapping(path="/delete/{id}")
    public @ResponseBody String deleteProduct(@PathVariable Long id) {
        Optional<Product> optionalProduct = productRepository.findById(id); // returns empty instance if entity with given ID not found
    if(optionalProduct.isPresent()) { 
        productRepository.deleteById(id);
        return "Deleted";
    }
    else
    {
        return "Product not found";
    }
    }
   
    @PutMapping(path="/update/{id}")
    public @ResponseBody String updateProduct(@PathVariable Long id, @RequestParam String name, @RequestParam String author) {
        Optional<Product> optionalProduct = productRepository.findById(id); // returns empty instance if entity with given ID not found
    if(optionalProduct.isPresent()) { // isPresent() method is used to check optional returns True if value present else retuns False 
        Product p = optionalProduct.get();
        p.setName(name);
        p.setAuthor(author);
        productRepository.save(p);
        return "Updated";
    }
    else
    {
        return("Product not found, please create new product");
    }
    }

    @DeleteMapping(path="/deleteAll")
    public @ResponseBody String deleteAllProducts() {
        productRepository.deleteAll();
        return "All products deleted";
    }
}
