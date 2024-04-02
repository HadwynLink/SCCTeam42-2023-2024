using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class selectionDisplay : MonoBehaviour
{
    public TextMeshProUGUI text;
    public Slider targetSlider;
    public string suffix;

    public void updateDisplay()
    {
        text.text = targetSlider.value + suffix;
    }
}
