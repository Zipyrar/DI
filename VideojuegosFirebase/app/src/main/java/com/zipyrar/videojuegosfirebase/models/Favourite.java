package com.zipyrar.videojuegosfirebase.models;

public class Favourite {
    private String titulo;
    private String descripcion;
    private String imagen;
    private String id;

    public Favourite() {}

    public Favourite(String titulo, String descripcion, String imagen) {
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

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
}
