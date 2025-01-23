package com.zipyrar.videojuegosfirebase.viewmodels;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

import com.zipyrar.videojuegosfirebase.models.User;
import com.zipyrar.videojuegosfirebase.repositories.UserRepository;

public class RegisterViewModel extends ViewModel {
    private final UserRepository userRepository;

    //LiveData para manejar los resultados del registro.
    private final MutableLiveData<Boolean> registrationResult = new MutableLiveData<>();
    private final MutableLiveData<String> errorMessage = new MutableLiveData<>();

    public RegisterViewModel() {
        userRepository = new UserRepository();
    }

    public LiveData<Boolean> getRegistrationResult() {
        return registrationResult;
    }

    public LiveData<String> getErrorMessage() {
        return errorMessage;
    }

    public void registerUser(String email, String password, String confirmP, String name, String phone, String direction) {
        //Validación de datos.
        if (email.isEmpty() || password.isEmpty() || confirmP.isEmpty() ||
                name.isEmpty() || phone.isEmpty() || direction.isEmpty()) {
            errorMessage.setValue("Por favor, completa todos los campos.");
            return;
        }

        if (!password.equals(confirmP)) {
            errorMessage.setValue("Las contraseñas no coinciden.");
            return;
        }

        if (password.length() < 6) {
            errorMessage.setValue("La contraseña debe tener al menos 6 caracteres.");
            return;
        }

        //Crear el objeto User.
        User user = new User(name, phone, direction);

        //Llamar al repositorio para registrar al usuario.
        userRepository.registerUser(email, password, user).observeForever(result -> {
            if (result != null && result) {
                registrationResult.setValue(true);
            } else {
                errorMessage.setValue("Error en el registro. Por favor, inténtalo de nuevo.");
            }
        });
    }
}

