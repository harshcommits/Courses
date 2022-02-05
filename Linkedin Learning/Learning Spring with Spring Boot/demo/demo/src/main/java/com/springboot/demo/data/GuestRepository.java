package com.springboot.demo.data;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Date;

@Repository
public interface GuestRepository extends JpaRepository<Guest, Long> {
}
