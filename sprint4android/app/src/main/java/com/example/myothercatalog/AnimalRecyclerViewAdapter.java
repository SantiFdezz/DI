package com.example.myothercatalog;

import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class AnimalRecyclerViewAdapter  extends RecyclerView.Adapter<AnimalViewHolder> {
    private List<AnimalData> allTheData;
    private Activity activity;

    public AnimalRecyclerViewAdapter(List<AnimalData> dataSet, Activity activity){
        this.allTheData = dataSet;
        this.activity = activity;
    }
    public AnimalViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType){
        View view = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.animal_view_holder, parent, false);
        return new AnimalViewHolder(view);
    }
    public void onBindViewHolder(AnimalViewHolder holder, int position){
        AnimalData dataInPositionToBeRendered = allTheData.get(position);
        holder.showData(dataInPositionToBeRendered, activity);
    }
    public int getItemCount(){
        return allTheData.size();
    }

}
