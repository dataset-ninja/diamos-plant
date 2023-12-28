## Dataset Release and Comparative Analysis

The authors of the dataset contribute to the evolving field of foliar disease classification and recognition through the utilization of machine and deep learning concepts. DiaMOS Plant dataset compre 3505 images of pear fruit and leaves affected by four diseases.

| **DiaMOS Plant Dataset**     |                                                       |
| ---------------------------- | ----------------------------------------------------- |
| **Plant**                    | Pear                                                  |
| **Cultivar**                 | Septoria Piricola                                     |
| **Data Source Location**     | Sardegna, Italy                                       |
| **Type of Data**             | RGB Images                                            |
| **Annotation**               | csv, YOLO                                             |
| **ROI (Region of Interest)** | Leaf, Fruit                                           |
| **Total Size**               | 3505 images                                           |
|                              | (3006 leaves images +                                 |
|                              | 499 fruit images)                                     |
| **Data Accessibility**       | [Zenodo Link](https://doi.org/10.5281/zenodo.5557313) |
| **Accessed on**              | 17 October 2021                                       |
| **Application**              | Suitable for machine and                              |
|                              | deep learning tasks,                                  |
|                              | including image detection                             |
|                              | and classification                                    |

Additionally, a comparative analysis of existing literature datasets for leaf disease classification is conducted, emphasizing features that enhance the value and information content of the collected data. The study offers valuable guidelines for the research community in selecting and constructing datasets.
Significance of Leaf Analysis in Plant Health. The direct visual examination of leaves serves as a crucial source of information for assessing plant health. Leaf symptoms act as early indicators of various diseases, infections, parasites, and deficiencies that impact plant development and life cycles. Biotic and abiotic stresses, significant factors limiting agricultural productivity, necessitate innovative and sustainable cultivation practices.

## Role of ICT and AI in Agriculture

In addressing economic and environmental challenges, the adoption of Information and Communication Technologies (ICT) becomes pivotal. Proximity sensors, mobile applications, and AI integration assist farmers in cultivation practices, contributing to sustainable actions. Artificial Intelligence, particularly Computer Vision, plays a crucial role in early prediction and diagnosis by recognizing visible symptoms. The study categorizes models into forecast and diagnostic tasks, emphasizing the application of convolutional neural networks.
The accuracy of integrated AI systems depends on the quality of the training dataset. Developing intelligent neural networks requires substantial data, posing challenges in acquisition, annotation, and categorization. The availability of datasets in Digital Agriculture remains a challenge, hindering scientific progress.

## Survey of Existing Datasets

Recent years have witnessed efforts in data collection, with PlantVillage being a notable dataset. However, datasets created under controlled conditions may lack representativeness for real-world applications. The paper introduces DiaMOS Plant as a new dataset, emphasizing its collection under realistic field conditions. The survey aims to guide researchers in selecting datasets by providing a comprehensive analysis of publicly available datasets.

## Description

DiaMOS Plant is introduced as a field dataset for diagnosing and monitoring plant symptoms. It covers an entire growing season of a pear tree, containing 3505 images depicting four leaf stresses and three stages of fruit development. The dataset, suitable for machine and deep learning methods, includes detailed information on fruit and leaf images, resolution variations, and acquisition devices.
The dataset comprises images captured using different devices, including smartphones and DSLR cameras. Two resolutions, 2976 × 3968 and 3456 × 5184, add complexity and value to the dataset. Multiple devices were employed to simulate real-world scenarios where operators have diverse technical characteristics in their devices. Leaves were captured from the adaxial side under various realistic conditions, including different lighting, angles, backgrounds, and noise levels. This approach allowed for the representation of leaves under diverse lighting conditions and the observation of symptom evolution over time.

|                  | Smartphone Camera | DSRL Camera   |
| ---------------- | ----------------- | ------------- |
| **Image size**   | 2976 × 3968       | 3456 × 5184   |
| **Model device** | Honor 6×          | Canon EOS 60D |
| **Focal length** | 3.83 mm           | 50 mm         |
| **Focal ratio**  | f/2.2             | f/4.5         |
| **Color space**  | RGB               | RGB           |

## Disease Recognition and Annotation

The dataset labeling process involved manual annotation using the LabelImg software. An expert assisted in disease recognition, and severity levels were assigned for specific classes. Severity levels ranged from no risk (0%) to high risk (>50%), providing detailed information on the affected leaf area.
The dataset's representativeness, complexity, and detailed annotations contribute to its potential for advancing research in the field of plant symptom diagnosis and monitoring.
