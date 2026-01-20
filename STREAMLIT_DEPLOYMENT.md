# 🚀 Deploy MovieFlix on Streamlit Cloud

This guide explains how to deploy the MovieFlix Streamlit application on Streamlit Cloud for free.

---

## Prerequisites

✅ GitHub account (already pushed!)
✅ Streamlit Cloud account
✅ Heroku account (for backend deployment)

---

## Step 1: Deploy Backend to Heroku

### 1.1 Install Heroku CLI

```bash
# macOS
brew install heroku/brew/heroku

# Ubuntu/Debian
curl https://cli-assets.heroku.com/install-ubuntu.sh | sh

# Windows
choco install heroku-cli
```

### 1.2 Create Heroku App

```bash
cd /path/to/recommendation/backend
heroku login
heroku create your-app-name-backend
```

### 1.3 Create Procfile

```bash
# In backend/ directory
echo "web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app" > Procfile
```

### 1.4 Update requirements.txt

```bash
cd /path/to/recommendation/backend
pip install gunicorn
pip freeze > requirements.txt
```

### 1.5 Push to Heroku

```bash
git push heroku main
```

**Get your backend URL:**
```bash
heroku open  # Opens: https://your-app-name-backend.herokuapp.com
```

---

## Step 2: Update Streamlit App

Before deploying Streamlit, update `app.py` to use your Heroku backend:

```python
# In app.py, replace localhost with Heroku URL:
BACKEND_URL = "https://your-app-name-backend.herokuapp.com"
```

---

## Step 3: Deploy to Streamlit Cloud

### 3.1 Go to Streamlit Cloud

- Navigate to: https://streamlit.io/cloud
- Click "Sign up" (use GitHub account)

### 3.2 Deploy Your App

1. Click "New app"
2. Select your repository: `Nepalimovierecommendation`
3. Select branch: `main`
4. Select file path: `app.py`
5. Click "Deploy"

---

## Step 4: Configure Streamlit Cloud Settings

In Streamlit Cloud dashboard:

1. Go to your app settings
2. Click "Advanced settings"
3. Set environment variables:
   ```
   BACKEND_URL=https://your-app-name-backend.herokuapp.com
   ```

---

## Step 5: Test Live App

- Your app URL: `https://[username]-movieflix.streamlit.app`
- Test movie selection and recommendations
- Check backend connection

---

## Common Issues

### Backend Connection Error

```
ConnectionError: Failed to connect to backend
```

**Solution:**
- Verify Heroku app is running: `heroku logs -a your-app-name-backend`
- Update BACKEND_URL in Streamlit app settings
- Check CORS configuration in backend/main.py

### Port Issues

```
Address already in use
```

**Solution:**
- Use different port: `streamlit run app.py --server.port=8502`
- Kill existing process: `pkill -f streamlit`

### Slow Startup

**Solution:**
- ML model is pre-loaded on first request
- Subsequent requests will be faster
- Consider caching in Streamlit (@st.cache_resource)

---

## Step 6: Custom Domain (Optional)

1. Go to Streamlit Cloud app settings
2. Add custom domain in "App URL" section
3. Update DNS records at your domain registrar

---

## Monitoring & Logs

### View Streamlit Logs
```bash
# In Streamlit Cloud dashboard -> View logs
```

### View Heroku Logs
```bash
heroku logs -a your-app-name-backend --tail
```

### Stream Real-time Logs
```bash
heroku logs -a your-app-name-backend -f
```

---

## Update Deployment

### Push New Changes

```bash
# Local changes
git add .
git commit -m "Update feature"
git push origin main
```

### Auto-Deploy

Streamlit Cloud automatically redeploys when you push to GitHub!

### Manual Redeploy

1. Go to Streamlit Cloud dashboard
2. Click app menu (⋮) → Rerun

---

## Performance Tips

1. **Cache Heavy Computations**
   ```python
   @st.cache_resource
   def load_model():
       return expensive_operation()
   ```

2. **Optimize Images**
   - Use PNG format
   - Compress images under 1MB each

3. **Stream Large Data**
   ```python
   with st.spinner('Loading...'):
       # Long operation
   ```

4. **Use Session State**
   ```python
   if 'key' not in st.session_state:
       st.session_state.key = value
   ```

---

## Costs

| Service | Free Tier | Cost |
|---------|-----------|------|
| Streamlit Cloud | 3 apps | Free |
| Heroku Dynos | 550 free hours/month | $7+/month |
| Total | - | ~$7/month |

---

## Alternative: Deploy Backend on Railway

Simpler than Heroku (more free hours):

1. Go to https://railway.app
2. Connect GitHub repo
3. Deploy `backend/` directory
4. Get public URL
5. Update Streamlit app

---

## Final Checklist

- [ ] Backend deployed to Heroku/Railway
- [ ] Backend URL tested
- [ ] app.py updated with backend URL
- [ ] Code pushed to GitHub
- [ ] Streamlit Cloud app created
- [ ] Environment variables set
- [ ] App tested live
- [ ] Custom domain configured (optional)

---

## Support

For issues:
1. Check Streamlit Cloud logs
2. Check Heroku/Railway logs
3. Test backend API directly: `curl https://your-backend-url/health`
4. Verify CORS settings in backend

---

**Your MovieFlix app is now live on Streamlit Cloud! 🎉**

Share your app URL: `https://[username]-movieflix.streamlit.app`
