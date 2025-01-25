package com.zipyrar.videojuegosfirebase.viewmodels;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

import com.zipyrar.videojuegosfirebase.repositories.UserRepository;

public class LoginViewModel extends ViewModel {
    private final UserRepository userRepository;
    private final MutableLiveData<Boolean> loginResult = new MutableLiveData<>();
    private final MutableLiveData<String> errorMessage = new MutableLiveData<>();

    public LoginViewModel() {
        userRepository = new UserRepository();
    }

    public LiveData<Boolean> getLoginResult() {
        return loginResult;
    }

    public LiveData<String> getErrorMessage() {
        return errorMessage;
    }

    public void loginUser(String email, String password) {
        if (email.isEmpty() || password.isEmpty()) {
            errorMessage.setValue("Por favor, completa todos los campos.");
            return;
        }

        userRepository.loginUser(email, password).observeForever(result -> {
            if (result != null && result) {
                loginResult.setValue(true);
            } else {
                errorMessage.setValue("Error en autenticación. Verifica tus credenciales.");
            }
        });
    }
}
