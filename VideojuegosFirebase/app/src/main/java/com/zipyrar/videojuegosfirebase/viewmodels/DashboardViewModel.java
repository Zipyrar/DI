package com.zipyrar.videojuegosfirebase.viewmodels;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.ViewModel;

import com.zipyrar.videojuegosfirebase.models.Videogame;
import com.zipyrar.videojuegosfirebase.repositories.DashboardRepository;

import java.util.List;

public class DashboardViewModel extends ViewModel {
    private DashboardRepository repository;
    private LiveData<List<Videogame>> videogames;

    public DashboardViewModel() {
        repository = new DashboardRepository();
        videogames = repository.getVideogames();
    }

    public LiveData<List<Videogame>> getVideogames() {
        return videogames;
    }
}
