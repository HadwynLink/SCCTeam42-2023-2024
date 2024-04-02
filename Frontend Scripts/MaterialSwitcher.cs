using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class MaterialSwitcher : MonoBehaviour
{
    GameManager manager;

    public Material water;
    public Material aluminum;
    public Material concrete;
    public Material lead;
    public Material kapton;
    public Material polythylene;

    public Material Proton;
    public Material Photon;
    public Material Electron;
    public Material Gamma;
    public Material Neon;
    public Material Carbon;

    public Material ProtonTrail;
    public Material PhotonTrail;
    public Material ElectronTrail;
    public Material GammaTrail;
    public Material NeonTrail;
    public Material CarbonTrail;

    public MeshRenderer currentMat;
    public TextMeshProUGUI matText;

    // Start is called before the first frame update
    void Start()
    {
        manager = GameObject.FindGameObjectWithTag("GameManager").GetComponent<GameManager>();

        switch (manager.WallMat)
        {
            case 0:
                currentMat.material = water;
                matText.text = "Barrier Type: Water";
                break;
            case 1:
                currentMat.material = aluminum;
                matText.text = "Barrier Type: Aluminum";
                break;
            case 2:
                currentMat.material = concrete;
                matText.text = "Barrier Type: Concrete";
                break;
            case 3:
                currentMat.material = lead;
                matText.text = "Barrier Type: Lead";
                break;
            case 4:
                currentMat.material = kapton;
                matText.text = "Barrier Type: Kapton";
                break;
            default:
                currentMat.material = polythylene;
                matText.text = "Barrier Type: Polythylene";
                break;
        }
    }
}
