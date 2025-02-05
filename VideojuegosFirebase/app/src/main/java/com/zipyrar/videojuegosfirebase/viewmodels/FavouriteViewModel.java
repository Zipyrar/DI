package com.zipyrar.videojuegosfirebase.viewmodels;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.ViewModel;

import com.zipyrar.videojuegosfirebase.models.Favourite;
import com.zipyrar.videojuegosfirebase.repositories.FavouriteRepository;

import java.util.List;

public class FavouriteViewModel extends ViewModel {
    private final FavouriteRepository repository;
    private final LiveData<List<Favourite>> favourites;

    public FavouriteViewModel() {
        repository = new FavouriteRepository();
        favourites = repository.getUserFavourites();
    }

    public LiveData<List<Favourite>> getFavourites() {
        return favourites;
    }

    public LiveData<Boolean> addFavourite(String videogameId, Favourite favourite) {
        return repository.addFavourite(videogameId, favourite);
    }

    public LiveData<Boolean> removeFavourite(String videogameId) {
        return repository.removeFavourite(videogameId);
    }
}