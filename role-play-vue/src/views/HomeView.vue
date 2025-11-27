<template>
  <div class="home-container">
    <div class="stars"></div>
    <div class="grid-bg"></div>
    
    <div class="hero-section">
      <div class="hero-glow"></div>
      <h1 class="hero-title">AI虚拟角色</h1>
      <p class="hero-subtitle">进入元宇宙，与虚拟角色对话</p>
      <router-link to="/roles" class="cta-button">
        <span class="button-text">进入</span>
        <span class="button-glow"></span>
      </router-link>
    </div>
    
    <div class="features-section">
      <div class="feature-card">
        <div class="card-border"></div>
        <div class="feature-icon">🎭</div>
        <h3>虚拟角色</h3>
        <p>多元化虚拟人物</p>
      </div>
      
      <div class="feature-card">
        <div class="card-border"></div>
        <div class="feature-icon">🤖</div>
        <h3>AI驱动</h3>
        <p>智能对话引擎</p>
      </div>
      
      <div class="feature-card">
        <div class="card-border"></div>
        <div class="feature-icon">💫</div>
        <h3>沉浸体验</h3>
        <p>未来交互方式</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeView'
}
</script>

<style scoped>
@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-20px); }
}

@keyframes glow {
  0%, 100% { box-shadow: 0 0 20px rgba(102, 126, 234, 0.5), inset 0 0 20px rgba(102, 126, 234, 0.1); }
  50% { box-shadow: 0 0 40px rgba(102, 126, 234, 0.8), inset 0 0 20px rgba(102, 126, 234, 0.2); }
}

@keyframes scan {
  0% { transform: translateY(-100%); }
  100% { transform: translateY(100%); }
}

.home-container {
  min-height: 100vh;
  background: #0a0e27;
  padding: 2rem 1rem;
  position: relative;
  overflow: hidden;
}

.stars {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: 
    radial-gradient(2px 2px at 20px 30px, #eee, rgba(0,0,0,0)),
    radial-gradient(2px 2px at 60px 70px, #fff, rgba(0,0,0,0)),
    radial-gradient(1px 1px at 50px 50px, #fff, rgba(0,0,0,0)),
    radial-gradient(1px 1px at 130px 80px, #fff, rgba(0,0,0,0)),
    radial-gradient(2px 2px at 90px 10px, #fff, rgba(0,0,0,0));
  background-repeat: repeat;
  background-size: 200px 200px;
  pointer-events: none;
  z-index: 1;
}

.grid-bg {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: 
    linear-gradient(0deg, transparent 24%, rgba(102, 126, 234, 0.05) 25%, rgba(102, 126, 234, 0.05) 26%, transparent 27%, transparent 74%, rgba(102, 126, 234, 0.05) 75%, rgba(102, 126, 234, 0.05) 76%, transparent 77%, transparent),
    linear-gradient(90deg, transparent 24%, rgba(102, 126, 234, 0.05) 25%, rgba(102, 126, 234, 0.05) 26%, transparent 27%, transparent 74%, rgba(102, 126, 234, 0.05) 75%, rgba(102, 126, 234, 0.05) 76%, transparent 77%, transparent);
  background-size: 50px 50px;
  pointer-events: none;
  z-index: 1;
}

.hero-section {
  text-align: center;
  padding: 3rem 1rem;
  margin-bottom: 2rem;
  color: white;
  position: relative;
  z-index: 10;
}

.hero-glow {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 300px;
  height: 300px;
  background: radial-gradient(circle, rgba(102, 126, 234, 0.3) 0%, transparent 70%);
  border-radius: 50%;
  filter: blur(40px);
  pointer-events: none;
}

.hero-title {
  font-size: 2.5rem;
  font-weight: 900;
  margin-bottom: 0.8rem;
  letter-spacing: 2px;
  text-shadow: 0 0 20px rgba(102, 126, 234, 0.8);
  background: linear-gradient(135deg, #00d4ff 0%, #667eea 50%, #ff00ff 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-subtitle {
  font-size: 1rem;
  color: rgba(102, 126, 234, 0.9);
  margin-bottom: 2rem;
  font-weight: 400;
  letter-spacing: 1px;
}

.cta-button {
  display: inline-block;
  position: relative;
  background: transparent;
  color: #00d4ff;
  padding: 0.8rem 2rem;
  border: 2px solid #00d4ff;
  border-radius: 5px;
  text-decoration: none;
  font-weight: 700;
  font-size: 0.9rem;
  transition: all 0.3s ease;
  letter-spacing: 1px;
  overflow: hidden;
  z-index: 2;
}

.button-text {
  position: relative;
  z-index: 2;
}

.button-glow {
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(0, 212, 255, 0.3), transparent);
  transition: left 0.5s ease;
}

.cta-button:hover {
  box-shadow: 0 0 20px rgba(0, 212, 255, 0.6), inset 0 0 20px rgba(0, 212, 255, 0.1);
  color: #00d4ff;
}

.cta-button:hover .button-glow {
  left: 100%;
}

.features-section {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-top: 2rem;
  max-width: 1000px;
  margin-left: auto;
  margin-right: auto;
  position: relative;
  z-index: 10;
}

.feature-card {
  background: rgba(15, 23, 42, 0.8);
  backdrop-filter: blur(10px);
  padding: 1.5rem;
  border-radius: 0;
  text-align: center;
  border: 1px solid rgba(102, 126, 234, 0.3);
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.card-border {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, transparent, #00d4ff, transparent);
  animation: scan 3s linear infinite;
}

.feature-card:hover {
  border-color: #00d4ff;
  box-shadow: 0 0 20px rgba(0, 212, 255, 0.3), inset 0 0 20px rgba(0, 212, 255, 0.05);
  transform: translateY(-5px);
}

.feature-icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  display: inline-block;
  animation: float 3s ease-in-out infinite;
}

.feature-card h3 {
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
  color: #00d4ff;
  font-weight: 700;
  letter-spacing: 1px;
}

.feature-card p {
  color: rgba(102, 126, 234, 0.8);
  font-size: 0.85rem;
  line-height: 1.5;
  font-weight: 400;
}
</style>