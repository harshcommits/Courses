package com.spring.demoapp.student;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository //responsible for data access
public interface StudentRepository extends JpaRepository<Student, Long> {  //id type is long for student

    @Query("SELECT s FROM Student s WHERE s.email = ?1")  //JDQL using @Entity from Student; not SQL
    Optional<Student> findStudentByEmail(String email);
}
