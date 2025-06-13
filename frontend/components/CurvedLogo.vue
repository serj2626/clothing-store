<template>
  <div class="logo-wrapper">
    <svg width="300" height="190" viewBox="0 0 300 200">
      <defs>
        <!-- Обратная дуга (снизу вверх) -->
        <path
          id="reverse-arc"
          d="M 50,100 A 100,100 0 0,0 250,100"
          fill="none"
        />
      </defs>
      <text
        fill="#e0bea2"
        font-size="36"
        font-weight="900"
        dominant-baseline="middle"
      >
        <textPath href="#reverse-arc" startOffset="50%" text-anchor="middle">
          ClothCrash
        </textPath>
      </text>
    </svg>
  </div>
</template>

<style scoped>
.logo-wrapper {
  display: flex;
  justify-content: center;
  padding-top: 30px;
  overflow: visible;

  position: absolute;
  top: 10px;
  left: 50%;
  transform: translateX(-50%);
}
</style>
