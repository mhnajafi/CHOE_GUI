/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.h
  * @brief          : Header for main.c file.
  *                   This file contains the common defines of the application.
  ******************************************************************************
  * @attention
  *
  * <h2><center>&copy; Copyright (c) 2021 STMicroelectronics.
  * All rights reserved.</center></h2>
  *
  * This software component is licensed by ST under BSD 3-Clause license,
  * the "License"; You may not use this file except in compliance with the
  * License. You may obtain a copy of the License at:
  *                        opensource.org/licenses/BSD-3-Clause
  *
  ******************************************************************************
  */
/* USER CODE END Header */

/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef __MAIN_H
#define __MAIN_H

#ifdef __cplusplus
extern "C" {
#endif

/* Includes ------------------------------------------------------------------*/
#include "stm32f1xx_hal.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Exported types ------------------------------------------------------------*/
/* USER CODE BEGIN ET */

/* USER CODE END ET */

/* Exported constants --------------------------------------------------------*/
/* USER CODE BEGIN EC */

/* USER CODE END EC */

/* Exported macro ------------------------------------------------------------*/
/* USER CODE BEGIN EM */

/* USER CODE END EM */

/* Exported functions prototypes ---------------------------------------------*/
void Error_Handler(void);

/* USER CODE BEGIN EFP */

/* USER CODE END EFP */

/* Private defines -----------------------------------------------------------*/
#define VL1_Pin GPIO_PIN_0
#define VL1_GPIO_Port GPIOB
#define VL2_Pin GPIO_PIN_1
#define VL2_GPIO_Port GPIOB
#define DIAG1_Pin GPIO_PIN_12
#define DIAG1_GPIO_Port GPIOB
#define DIR1_Pin GPIO_PIN_13
#define DIR1_GPIO_Port GPIOB
#define PWM1_Pin GPIO_PIN_14
#define PWM1_GPIO_Port GPIOB
#define DIR_Pin GPIO_PIN_10
#define DIR_GPIO_Port GPIOA
#define PWM_Pin GPIO_PIN_11
#define PWM_GPIO_Port GPIOA
#define DIAG_Pin GPIO_PIN_12
#define DIAG_GPIO_Port GPIOA
#define VL3_Pin GPIO_PIN_6
#define VL3_GPIO_Port GPIOB
#define VL4_Pin GPIO_PIN_7
#define VL4_GPIO_Port GPIOB
/* USER CODE BEGIN Private defines */

/* USER CODE END Private defines */

#ifdef __cplusplus
}
#endif

#endif /* __MAIN_H */

/************************ (C) COPYRIGHT STMicroelectronics *****END OF FILE****/
