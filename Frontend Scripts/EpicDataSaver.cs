using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class EpicDataSaver : MonoBehaviour
{
    GameManager manager;
    public int target;
    public TMP_Dropdown dropdown;
    public Slider slider;
    public selectionDisplay displayText;
    public TMP_InputField input;

    // Start is called before the first frame update
    void Start()
    {
        manager = GameObject.FindGameObjectWithTag("GameManager").GetComponent<GameManager>();
        dataLoadYay();
    }

    public void dataSaveYay()
    {
        switch (target)
        {
            case 0:
                manager.RadType = dropdown.value;
                break;
            case 1:
                manager.WallMat = dropdown.value;
                break;
            case 2:
                manager.subjectMass = slider.value;
                break;
            case 3:
                manager.subjectSA = slider.value;
                break;
            case 4:
                manager.RadSpeed = dropdown.value;
                break;
            case 5:
                if (float.TryParse(input.text, out _))
                {
                    manager.simSpeed = float.Parse(input.text);
                }
                else
                {
                    input.text = "";
                }
                break;
            default:
                break;
        }
    }
    public void dataLoadYay()
    {
        switch (target)
        {
            case 0:
                dropdown.value = manager.RadType;
                break;
            case 1:
                dropdown.value = manager.WallMat;
                break;
            case 2:
                slider.value = manager.subjectMass;
                displayText.updateDisplay();
                break;
            case 3:
                slider.value = manager.subjectSA;
                displayText.updateDisplay();
                break;
            case 4:
                dropdown.value = manager.RadSpeed;
                break;
            case 5:
                input.text = manager.simSpeed.ToString();
                break;
            default:
                break;
        }
    }
}
