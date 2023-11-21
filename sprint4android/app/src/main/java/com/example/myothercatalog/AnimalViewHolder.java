package com.example.myothercatalog;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;

import java.util.List;

public class AnimalViewHolder extends RecyclerView.ViewHolder {
    private final TextView textView;
    private final ImageView imageView;
    private List<AnimalData> allTheAnimals;

    public AnimalViewHolder(@NonNull View itemView){
        //Creamos el viewHolder e igualamos los datos
        super(itemView);
        textView = (TextView) itemView.findViewById(R.id.animal_name_text_view);
        imageView = (ImageView) itemView.findViewById(R.id.animal_image_view);
        //si clicka la celda itemview le lleva al a nueva activity
        itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openDetailActivity(getAdapterPosition(), itemView.getContext());
            }
        });

    }
    private void openDetailActivity(int position, Context context) {
        //AnimalData animalData = allTheAnimals.get(position);;
        Intent intent = new Intent(context, DetailActivity.class);
        //intent.putExtra("animalName", animalData.getName());
        //intent.putExtra("animalImageUrl", animalData.getImageUrl());
        context.startActivity(intent);
    }
    public void showData(AnimalData data, Activity activity){
        //Mostramos los datos
        textView.setText(data.getName());
        Glide.with(itemView.getContext())
                .load(data.getImageUrl())
                .into(imageView);
    }
}
