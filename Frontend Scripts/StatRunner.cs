using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class StatRunner : MonoBehaviour
{
    public GameManager manager;

    public TextMeshProUGUI radType;
    public TextMeshProUGUI radSpeed;



    // Start is called before the first frame update
    void Start()
    {
        manager = GameObject.FindGameObjectWithTag("GameManager").GetComponent<GameManager>();

        switch (manager.RadType)
        {
            case 0:
                radType.text = "Radiation Type: Gamma";
                break;
            case 1:
                radType.text = "Radiation Type: Carbon";
                break;
            case 2:
                radType.text = "Radiation Type: Neon";
                break;
            case 3:
                radType.text = "Radiation Type: Proton";
                break;
            default:
                break;
        }

        switch (manager.RadSpeed)
        {
            case 0:
                radSpeed.text = "Radiation Speed: Fast";
                break;
            case 1:
                radSpeed.text = "Radiation Speed: Slow";
                break;
            default:
                break;
        }
    }
}
