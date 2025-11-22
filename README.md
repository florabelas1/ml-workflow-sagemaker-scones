# ML Workflow for Scones Unlimited on Amazon SageMaker

**AWS Machine Learning Engineer Nanodegree - Production ML Pipeline Project**

End-to-end machine learning workflow using AWS SageMaker, Lambda Functions, and 
Step Functions for automated image classification in production environments.

---

## 🎯 Project Objective

Build a scalable, production-ready ML pipeline that:
1. Orchestrates image classification workflow using AWS Step Functions
2. Deploys ML model inference with SageMaker endpoints
3. Implements serverless functions with AWS Lambda
4. Filters predictions based on confidence thresholds
5. Demonstrates MLOps best practices for production deployment

**Business Case**: Scones Unlimited needs to automatically classify product images 
for quality control and inventory management.

---

## 🏗️ Architecture Overview
```
S3 Bucket (Image Storage)
    ↓
Lambda: serializeImageData
    ↓ (Base64 encoded image)
SageMaker Endpoint: Image Classification
    ↓ (Inference results)
Lambda: filterLowConfidence (threshold: 93%)
    ↓
Result (Pass/Fail)
```

**Orchestrated by AWS Step Functions State Machine**

---

## 🔧 AWS Services Used

| Service | Purpose |
|---------|---------|
| **Amazon SageMaker** | Model training and endpoint deployment |
| **AWS Lambda** | Serverless data processing and filtering |
| **AWS Step Functions** | Workflow orchestration and error handling |
| **Amazon S3** | Image storage and retrieval |
| **IAM** | Security and permissions management |

---

## 📁 Project Structure
```
├── starter.ipynb              # Main notebook with full workflow
├── Lambda.py                  # Three Lambda function implementations
├── testmachine.asl.json      # Step Functions state machine definition
├── step_function.png          # Workflow visualization
├── stepfunctions_graph.png    # State machine graph
├── steptests.png              # Testing results
└── README.md                  # This file
```

---

## 🔄 Workflow Components

### 1️⃣ Lambda: serializeImageData

**Purpose**: Fetch image from S3 and prepare for inference
```python
def lambda_handler(event, context):
    # Download image from S3
    # Encode to base64
    # Return serialized data
```

**Input**: S3 bucket and key  
**Output**: Base64-encoded image data

---

### 2️⃣ SageMaker Endpoint: Image Classification

**Purpose**: Run ML model inference

- **Model**: Pre-trained image classification model
- **Endpoint**: `image-classification-2025-09-19-19-15-12-655`
- **Input**: Base64 image data
- **Output**: Classification predictions with confidence scores

---

### 3️⃣ Lambda: classifier

**Purpose**: Invoke SageMaker endpoint and return predictions
```python
def lambda_handler(event, context):
    # Decode image data
    # Invoke SageMaker endpoint
    # Return inference results
```

---

### 4️⃣ Lambda: filterLowConfidence

**Purpose**: Quality gate - only accept high-confidence predictions
```python
THRESHOLD = 0.93

def lambda_handler(event, context):
    # Parse inference results
    # Check if max confidence >= 93%
    # Raise exception if below threshold
```

**Why 93%?** Ensures only high-quality predictions proceed to production use.

---

## 🚀 Deployment Steps

### 1. Setup SageMaker Notebook
```bash
# Launch SageMaker notebook instance
# Clone project repository
# Install dependencies
```

### 2. Train and Deploy Model
```python
# Train image classification model
# Deploy to SageMaker endpoint
# Note endpoint name for Lambda configuration
```

### 3. Create Lambda Functions
```bash
# Create 3 Lambda functions from Lambda.py
# Configure IAM roles (SageMaker, S3 access)
# Set environment variables (endpoint name, threshold)
```

### 4. Build Step Functions State Machine
```bash
# Upload testmachine.asl.json
# Configure Lambda function ARNs
# Set error handling and retry logic
```

### 5. Test the Workflow
```bash
# Upload test images to S3
# Execute Step Functions workflow
# Verify results and error handling
```

---

## 📊 Step Functions State Machine

### State Machine Definition (ASL)

The `testmachine.asl.json` defines:
- **States**: Serialize → Classify → Filter
- **Error Handling**: Retry logic and catch blocks
- **Timeouts**: Prevent hanging executions
- **Success/Failure paths**: Clear workflow outcomes

### Visual Workflow

See `step_function.png` and `stepfunctions_graph.png` for visual representation 
of the state machine flow.

---

## 🎓 Project Context

**Program**: AWS Machine Learning Engineer Nanodegree  
**Provider**: Udacity + AWS  
**Focus**: MLOps, Production ML, AWS Services Integration  
**Year**: 2025

### Learning Objectives Achieved

✅ Deploy ML models to production with SageMaker  
✅ Build serverless workflows with Lambda  
✅ Orchestrate complex pipelines with Step Functions  
✅ Implement quality gates and error handling  
✅ Design scalable, event-driven ML systems  
✅ Apply MLOps best practices  
✅ Manage AWS resources and IAM policies

---

## 🔍 Key Technical Concepts

### Serverless Architecture Benefits

- **Scalability**: Automatically handles varying loads
- **Cost-Effective**: Pay only for actual usage
- **Maintainability**: No server management required
- **Reliability**: Built-in redundancy and retries

### Step Functions Advantages

- **Visual Workflow**: Easy to understand and debug
- **Error Handling**: Automatic retries and catch blocks
- **State Management**: Tracks execution history
- **Integration**: Seamless AWS service coordination

### Confidence Thresholding

**Why filter low-confidence predictions?**
- Prevents incorrect classifications in production
- Maintains data quality standards
- Allows human review of uncertain cases
- Improves overall system reliability

---

## 📈 Production Considerations

### Monitoring & Logging

- **CloudWatch Logs**: Track Lambda executions
- **SageMaker Monitoring**: Model performance metrics
- **Step Functions History**: Workflow execution tracking
- **Alarms**: Alert on failures or threshold violations

### Cost Optimization

- **SageMaker Endpoints**: Use auto-scaling
- **Lambda**: Optimize memory allocation
- **S3**: Lifecycle policies for old images
- **Step Functions**: Minimize state transitions

### Security Best Practices

- **IAM Roles**: Principle of least privilege
- **Encryption**: S3 and SageMaker encryption at rest
- **VPC**: Network isolation for sensitive workloads
- **Secrets Manager**: Secure credential storage

---

## 🧪 Testing Strategy

### Unit Tests
- Individual Lambda function testing
- Mock SageMaker endpoint responses
- Validate data transformations

### Integration Tests
- Full Step Functions workflow execution
- Multiple image types and sizes
- Edge cases (corrupted images, network failures)

### Results
See `steptests.png` for successful test execution examples.

---

## 💡 Real-World Applications

This workflow pattern applies to:

- 📸 **E-commerce**: Product image classification
- 🏥 **Healthcare**: Medical image analysis pipelines
- 🚗 **Autonomous Vehicles**: Real-time object detection
- 📱 **Social Media**: Content moderation workflows
- 🏭 **Manufacturing**: Quality control automation

---

## 🎯 Future Enhancements

- [ ] Add A/B testing for model versions
- [ ] Implement model retraining pipeline
- [ ] Add data drift detection
- [ ] Create monitoring dashboard
- [ ] Implement batch inference option
- [ ] Add multi-model ensemble
- [ ] Integrate with CI/CD pipeline

---

## 🔗 Resources

- [AWS Step Functions Documentation](https://docs.aws.amazon.com/step-functions/)
- [SageMaker Inference Guide](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html)
- [Lambda Best Practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)
- [MLOps on AWS](https://aws.amazon.com/sagemaker/mlops/)

---

## 📸 Workflow Screenshots

### Step Functions Graph
![Step Functions Workflow](stepfunctions_graph.png)

### Execution Results
![Test Results](steptests.png)

---

*AWS Machine Learning Engineer Nanodegree - 2025*
