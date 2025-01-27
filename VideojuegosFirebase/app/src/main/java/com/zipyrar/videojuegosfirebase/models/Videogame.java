package com.zipyrar.videojuegosfirebase.models;

import java.io.Serializable;

public class Videogame implements Serializable{
    private String titulo;
    private String descripcion;
    private String imagen;

    public Videogame() {}

    public Videogame(String titulo, String descripcion, String imagen) {
        this.titulo = titulo;
        this.descripcion = descripcion;
        this.imagen = imagen;
    }

    public String getTitulo() {
        return titulo;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public String getImagen() {
        return imagen;
    }
}
