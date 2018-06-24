package gq.yigit.foodcloud;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class LearnMore extends AppCompatActivity implements View.OnClickListener {
    private static final String TAG = "MainActivity";
    public String prod_loc_more;
    public ImageView factory;
    public ImageView farm;
    public ImageView packaging;
    public ImageView trans1;
    public ImageView trans2;
    public ImageView factory_cond;
    public ImageView farm_cond;
    public ImageView packaging_cond;
    public ImageView trans1_cond;
    public ImageView trans2_cond;
    public Button back_to_main;
    public Map<String, Object> someMap;
    public String prod_loc;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        Bundle extras = getIntent().getExtras();
        if (extras != null) {
            prod_loc_more = extras.getString("key");
        }
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_learn_more);
        factory = (ImageView) findViewById(R.id.factory);
        factory.setOnClickListener(this);
        farm = (ImageView) findViewById(R.id.farm);
        farm.setOnClickListener(this);
        packaging = (ImageView) findViewById(R.id.packaging);
        packaging.setOnClickListener(this);
        trans1 = (ImageView) findViewById(R.id.trans1);
        trans1.setOnClickListener(this);
        trans2 = (ImageView) findViewById(R.id.trans2);
        trans2.setOnClickListener(this);
        back_to_main = (Button) findViewById(R.id.go_back_to_main);
        back_to_main.setOnClickListener(this);

    }

    public void onClick(View v){
        if(v.getId() == R.id.back_to_main){
            Intent i = new Intent(LearnMore.this, MainActivity.class);
            startActivity(i);
        }
    }
}
