package com.example.myothercatalog;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import com.bumptech.glide.Glide;

public class DetailActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);

        // Recuperar extras del intent
        Intent intent = getIntent();
        String animalName = intent.getStringExtra("animalName");
        String animalDescription = intent.getStringExtra("animalDescription");
        String animalImageUrl = intent.getStringExtra("animalImageUrl");

        // Mostrar datos en la interfaz de usuario
        TextView titleTextView = findViewById(R.id.detail_name_text_view);
        TextView descriptionTextView = findViewById(R.id.detail_desc_text_view);
        ImageView imageView = findViewById(R.id.detail_image_view);

        titleTextView.setText(animalName);
        descriptionTextView.setText(animalDescription);

        // Usa Glide para cargar la imagen
        Glide.with(this)
                .load(animalImageUrl)
                .circleCrop()
                .into(imageView);
    }
}