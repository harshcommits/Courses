package com.spring.demoapp.student;

import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.time.LocalDate;
import java.util.List;

import static java.time.Month.*;

@Configuration
public class StudentConfig {

    @Bean
    CommandLineRunner commandLineRunner(StudentRepository repository) {
        return args -> {
            Student harsh = new Student(
                    1L,
                    "Harsh",
                    "admin@example.com",
                    LocalDate.of(2000, JANUARY, 12)
            );

            Student alex = new Student(
                    2L,
                    "Alex",
                    "alex@example.com",
                    LocalDate.of(2010, JANUARY, 14)
            );

            repository.saveAll(
                    List.of(harsh, alex)
            );

        };
    }
}
