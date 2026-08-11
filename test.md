模型,完全正确(%),函数名+参数名(%),函数名(%),调用函数(%)
qwen-2.5,35.19,44.44,53.7,53.7
qwen2.5-SFT,77.78,90.74,98.15,100.0
qwen2.5-grpo,74.07,92.59,98.15,100.0
qwen2.5-sft-grpo,83.33,96.3,98.15,100.0
qwen2.5-sft-rl2,87.04,98.15,100.0,100.0
gemma,28.0,41.0,54.0,65.0
gemma-SFT,41.0,52.0,52.0,52.0

- SFT: lora_rank=16, num_train_epochs=3.0, 其余默认
- Grpo: actor_rollout_ref.rollout.n=8, trainer.total_epochs=3, actor_rollout_ref.actor.ppo_mini_batch_size=256
- 奖励设置
  - 【0.0】不调用函数 
  - 【0.5】调用函数 
  - 【1.0】函数名正确 
  - 【1.5】函数正确，参数名正确
  - 【2.0】函数正确，参数值正确

SMART_HOME_CATEGORIES = {
    "照明类": ["Light", "CeilingLight", "TableLamp", "FloorLamp", "NightLight", "DeskLamp"],
    "温控类": ["AC", "Fan", "Humidifier"],
    "娱乐类": ["TV", "Projector", "Speaker"],
    "厨电类": ["Fridge", "RiceCooker", "RangeHood", "Dishwasher", "Microwave", "CoffeeMaker", "Sterilizer"],
    "门窗类": ["Curtain", "Door", "Window"],
    "清洁类": ["RobotVacuum", "Washer"],
    "安防类": ["Camera"],
    "卫浴类": ["Toilet", "BathHeater", "Bathtub"]
}

# 数据样例

# tools
[
  {
    "type": "function",
    "function": {
      "name": "setBathHeaterTemperature",
      "description": "Set the temperature of the bath heater in the bathroom",
      "parameters": {
        "type": "object",
        "properties": {
          "temperature": {
            "description": "The desired temperature in degrees Celsius",
            "type": "number",
            "default": 20
          }
        }
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "turnOnNightLight",
      "description": "Turn on the night light in the bathroom",
      "parameters": {
        "type": "object",
        "properties": {
          "brightness": {
            "description": "The brightness level of the night light (0-100)",
            "type": "number",
            "default": 30
          }
        }
      }
    }
  }
]

# query
The bathroom is cold, heat it up to 25

# answer
{
  "name": "setBathHeaterTemperature",
  "arguments": {
    "temperature": 25
  }
}

# 提示词设置

  """You are a data generator for smart home function calling dataset. Generate one data entry in the following JSON format:

{
  "query": "a casual, conversational English instruction for smart home control",
  "answers": "[{\"name\": \"function_name\", \"arguments\": {...}}]",
  "tools": "[{\"name\": \"function_name\", \"description\": \"...\", \"parameters\": {...}}, ...]"
}

Requirements:
1. Instruction: Must be casual, conversational, and natural English. Should feel like everyday speech with natural redundancy and incomplete instructions. **MUST be declarative sentences (no interrogative sentences like "Can you...?" "Could you...?" "Will you...?")**. Examples:
   - "Hey, turn on the lights, the living room ones"
   - "Ugh it's so hot in here, set the temperature lower"
   - "The bedroom is too dark, make it brighter"
   - "Turn off that TV, I can't concentrate"
   - "I'm going to bed, turn everything off."
   - "The kitchen light is bothering me, turn off it."

2. Tools: Provide 2-4 function definitions in JSON schema format. Each function should follow this structure:
   {
     "name": "function_name",
     "description": "Clear description of what the function does",
     "parameters": {
       "param_name": {
         "description": "Parameter description",
         "type": "number" or "string" etc.,
         "default": "default_value_if_applicable"
       },
       ...
     }
   }
   
   Example tools format:
   {
     "name": "turnOnLight",
     "description": "Turn on a light device in a specific room",
     "parameters": {
       "room": {
         "description": "The room where the light is located, onr of [LivingRoom, Bedroom, Kitchen, Bathroom]",
         "type": "string"
       }
     }
   }

3. Answers: Provide 1-3 function calls that would answer the query. Each call should have:
   - name: function name matching one in tools
   - arguments: object with actual parameter values matching the function's parameters

Parameter Design Guidelines:
- Parameters should be designed based on the device type and its characteristics. For example:
  - Location parameters: Devices may have location information like "Floor: 1, room: LivingRoom" (with floor and room), or just "Bedroom" (room only without floor), or "Bathroom" (room only). Design location parameters flexibly based on the context - sometimes include floor information, sometimes just room name.
  - Device-specific parameters: For air conditioners (AC), include parameters like temperature (e.g., 16-32 degrees Celsius), mode (Cool, Heat, Dry, Fan, Auto), fan speed, etc. For lights, include brightness (0-100), color, color temperature, light mode, etc. For curtains, include opening level (0-100%). For TVs, include volume, channel, etc.
  - Make parameters realistic and relevant to the device's actual functionality. Don't add unnecessary parameters that don't make sense for the device.

Smart devices to use:
{devices}

IMPORTANT FORMAT REQUIREMENTS:
- The "answers" field must be a JSON string (escaped JSON array), e.g., "[{\"name\": \"turnOnLight\", \"arguments\": {\"room\": \"LivingRoom\"}}]"
- The "tools" field must be a JSON string (escaped JSON array), e.g., "[{\"name\": \"turnOnLight\", \"description\": \"...\", \"parameters\": {...}}]"
- Both answers and tools should be valid JSON when parsed, but stored as escaped strings in the output JSON

Output ONLY valid JSON object with these three fields: query, answers, tools. No markdown code blocks, no additional text."""