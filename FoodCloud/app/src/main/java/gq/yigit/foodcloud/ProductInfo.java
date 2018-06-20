package gq.yigit.foodcloud;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.TextView;
import android.widget.Button;
import com.google.firebase.database.*;
import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;
import android.view.View.OnClickListener;

public class ProductInfo extends AppCompatActivity implements OnClickListener {
    private static final String TAG = "MainActivity";
    private TextView Name;
    private TextView Cal;
    private TextView Cooked;
    private TextView Nutrients;
    private TextView BBD;
    private TextView Processed;
    private TextView Problematic;
    private TextView Allergens;
    private String name;
    private String  cal;
    private String cooked;
    private ArrayList nutrients;
    private String bbd;
    private String processed;
    private String problematic;
    private ArrayList allergens;
    public ArrayList Prods;
    public Map<String, Object> someMap;
    public HashMap<String, Object> Prod;
    private Button scanBtn;
    private Button jrnyBtn;
    public String prod_loc;
    public String allergens_print = new String();
    public String nutrients_print = new String();



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_product_info);

    }

    @Override
    public void onClick(View v){
        if (v.getId() == R.id.button) {
            Intent i = new Intent(ProductInfo.this, MainActivity.class);
            startActivity(i);
        }if (v.getId() == R.id.journey) {
            Intent i = new Intent(ProductInfo.this, LearnMore.class);
            i.putExtra("key", prod_loc);
            startActivity(i);
        }
    }

    public void onStart(){
        super.onStart();
        setContentView(R.layout.activity_product_info);
        Map<String, String> map = new HashMap<String, String>();
        FirebaseDatabase database = FirebaseDatabase.getInstance();
        DatabaseReference myRef = database.getReference();
        scanBtn = (Button)findViewById(R.id.button);
        scanBtn.setOnClickListener(this);
        jrnyBtn = (Button)findViewById(R.id.journey);
        jrnyBtn.setOnClickListener(this);
        myRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {
                Bundle extras = getIntent().getExtras();
                if (extras != null) {
                    prod_loc = extras.getString("key");
                    //The key argument here must match that used in the other activity
                }
                // This method is called once with the initial value and again
                // whenever data at this location is updated.
                someMap = (Map<String, Object>) dataSnapshot.getValue();
                ArrayList al1 = new ArrayList();
                al1 = (ArrayList) someMap.get("Products");
                al1.remove(0);
                Prods = al1;
                Prod = (HashMap<String, Object>)al1.get((Integer.parseInt(prod_loc))-1);
                Log.d(TAG,"Value is : " + al1.get((Integer.parseInt(prod_loc))-1));
                Log.d(TAG,Prod.get("Calories").getClass().toString());
                name = Prod.get("Prod_Name").toString();
                cal = Prod.get("Calories").toString();
                cooked = Prod.get("Cooked").toString();
                nutrients = (ArrayList)Prod.get("Nutrients");
                bbd = Prod.get("BBD").toString();
                processed = Prod.get("Process").toString();
                allergens = (ArrayList)Prod.get("Allergens");
                problematic = Prod.get("Problematic").toString();
                Name = (TextView) findViewById(R.id.name);
                Name.setText("Name : " + name);
                Cal = (TextView) findViewById(R.id.Calories);
                Cal.setText("Calories : " + cal);
                Allergens = (TextView) findViewById(R.id.allergens);
                allergens_print = "";
                if(allergens.isEmpty()) {
                    Allergens.setText("Allergens : None");
                }else{
                    for(int i = 0; i < allergens.size();i++) {
                        allergens_print = allergens_print + allergens.get(i);
                        if(i != allergens.size() -1){
                            allergens_print = allergens_print + " , ";
                        }
                    }
                    Allergens.setText("Allergens : " + allergens_print);
                }
                Nutrients = (TextView) findViewById(R.id.nutrients);
                nutrients_print = "";
                if(nutrients.isEmpty()) {
                    Nutrients.setText("Nutrients : None");
                }else{
                    for(int i = 0; i < nutrients.size();i++) {
                        nutrients_print = nutrients_print + nutrients.get(i);
                        if(i != nutrients.size() -1){
                            nutrients_print = nutrients_print + " , ";
                        }
                    }
                    Nutrients.setText("Nutrients : " + nutrients_print);
                }
                Cooked = (TextView) findViewById(R.id.cooked);
                Cooked.setText("Cooked : " + cooked);
                BBD = (TextView) findViewById(R.id.BBD);
                BBD.setText("BBD : " +bbd);
                Processed = (TextView) findViewById(R.id.Process);
                Processed.setText("Process : " + processed);
                Problematic = (TextView) findViewById(R.id.Problems);
                Problematic.setText("Problemed : " + problematic);

            }

            @Override
            public void onCancelled(DatabaseError error) {
                // Failed to read value
                Log.w(TAG, "Failed to read value.", error.toException());
            }

        });







    }

}
