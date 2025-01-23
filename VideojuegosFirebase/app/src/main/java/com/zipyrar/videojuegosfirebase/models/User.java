package com.zipyrar.videojuegosfirebase.models;

public class User {
    private String name;
    private String phone;
    private String direction;

    public User() {}

    public User(String name, String phone, String direction) {
        this.name = name;
        this.phone = phone;
        this.direction = direction;
    }

    public String getName() {
        return name;
    }

    public String getPhone() {
        return phone;
    }

    public String getDirection() {
        return direction;
    }
}
