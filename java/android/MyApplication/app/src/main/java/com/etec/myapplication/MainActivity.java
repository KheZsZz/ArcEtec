package com.etec.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    TextView result;
    EditText v1;
    EditText v2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        v1 = findViewById(R.id.txt_firstNumber);
        v2 = findViewById(R.id.txt_secondNumber);


        findViewById(R.id.btn_soma).setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                if(v1.getText().toString().equals("") | v2.getText().toString().equals("")){
                    Toast.makeText(getApplicationContext(), "Valores nulos", Toast.LENGTH_SHORT).show();
                } else {
                    soma(Double.parseDouble(v1.getText().toString()), Double.parseDouble(v2.getText().toString()));
                }
            }
        });
        findViewById(R.id.btn_sub).setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                if(v1.getText().toString().equals("") | v2.getText().toString().equals("")){
                    Toast.makeText(getApplicationContext(), "Valores nulos", Toast.LENGTH_SHORT).show();
                } else {
                    sub(Double.parseDouble(v1.getText().toString()), Double.parseDouble(v2.getText().toString()));
                }
            }
        });
        findViewById(R.id.btn_mult).setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                if(v1.getText().toString().equals("") | v2.getText().toString().equals("")){
                    Toast.makeText(getApplicationContext(), "Valores nulos", Toast.LENGTH_SHORT).show();
                } else {
                    mult(Double.parseDouble(v1.getText().toString()), Double.parseDouble(v2.getText().toString()));
                }
            }
        });
        findViewById(R.id.btn_div).setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                if(v1.getText().toString().equals("") | v2.getText().toString().equals("")){
                    Toast.makeText(getApplicationContext(), "Valores nulos", Toast.LENGTH_SHORT).show();
                } else {
                    div(Double.parseDouble(v1.getText().toString()), Double.parseDouble(v2.getText().toString()));
                }
            }
        });
        findViewById(R.id.btn_sair).setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                finish();
            }
        });

    }

    public void soma(Double v1, Double v2) {
        Double res = v1 + v2;
        result = findViewById(R.id.lbl_result);
        result.setText("Resultado: " + res);
    }
    public void sub(Double v1, Double v2) {
        Double res = v1 - v2;
        result = findViewById(R.id.lbl_result);
        result.setText("Resultado: " + res);
    }public void mult(Double v1, Double v2) {
        Double res = v1 * v2;
        result = findViewById(R.id.lbl_result);
        result.setText("Resultado: " + res);
    }public void div(Double v1, Double v2) {
        Double res = v1 / v2;
        result = findViewById(R.id.lbl_result);
        result.setText("Resultado: " + res);
    }
}
