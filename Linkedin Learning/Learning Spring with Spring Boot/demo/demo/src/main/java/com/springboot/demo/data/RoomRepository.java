package com.springboot.demo.data;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository    //added for clarity that this is a repository
public interface RoomRepository extends CrudRepository<Room, Long> {
}
