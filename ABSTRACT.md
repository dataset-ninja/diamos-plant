The authors of the **DiaMOS Plant: A Dataset for Diagnosis and Monitoring Plant Disease** contribute to the evolving field of foliar disease classification and recognition through the utilization of machine and deep learning concepts. DiaMOS Plant dataset compre 3505 images of pear fruit and leaves affected by four diseases.
The study offers valuable guidelines for the research community in selecting and constructing datasets.
Significance of Leaf Analysis in Plant Health. The direct visual examination of leaves serves as a crucial source of information for assessing plant health. Leaf symptoms act as early indicators of various diseases, infections, parasites, and deficiencies that impact plant development and life cycles. Biotic and abiotic stresses, significant factors limiting agricultural productivity, necessitate innovative and sustainable cultivation practices.
DiaMOS Plant is introduced as a field dataset for diagnosing and monitoring plant symptoms. It covers an entire growing season of a pear tree, containing 3505 images depicting four leaf stresses and three stages of fruit development. The dataset, suitable for machine and deep learning methods, includes detailed information on fruit and leaf images, resolution variations, and acquisition devices.

| **DiaMOS Plant Dataset**     |                   |
| ---------------------------- | ----------------- |
| **Plant**                    | Pear              |
| **Cultivar**                 | Septoria Piricola |
| **Data Source Location**     | Sardegna, Italy   |
| **Type of Data**             | RGB Images        |
| **ROI (Region of Interest)** | Leaf, Fruit       |
| **Total Size**               | 3505 images       |

<span style="font-size: smaller; font-style: italic;">Dataset description</span>

## Dataset description

The authors of the dataset comprises images captured using different devices, including smartphones and DSLR cameras. Two resolutions, 2976 × 3968 and 3456 × 5184, add complexity and value to the dataset. Multiple devices were employed to simulate real-world scenarios where operators have diverse technical characteristics in their devices. Leaves were captured from the adaxial side under various realistic conditions, including different lighting, angles, backgrounds, and noise levels. This approach allowed for the representation of leaves under diverse lighting conditions and the observation of symptom evolution over time.

|                  | Smartphone Camera | DSRL Camera   |
| ---------------- | ----------------- | ------------- |
| **Image size**   | 2976 × 3968       | 3456 × 5184   |
| **Model device** | Honor 6×          | Canon EOS 60D |
| **Focal length** | 3.83 mm           | 50 mm         |
| **Focal ratio**  | f/2.2             | f/4.5         |
| **Color space**  | RGB               | RGB           |

<span style="font-size: smaller; font-style: italic;">Acquisition device configurations</span>

## Dataset annotation

The dataset labeling process involved manual annotation using the [LabelImg software](https://github.com/tzutalin/labelImg). An expert assisted in disease recognition, and severity levels were assigned for specific classes. Severity levels ranged from no risk (0%) to high risk (>50%), providing detailed information on the affected leaf area.
The dataset's representativeness, complexity, and detailed annotations contribute to its potential for advancing research in the field of plant symptom diagnosis and monitoring.
