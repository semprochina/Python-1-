  const container = document.querySelector('.container')
        const mirror = document.querySelector('.mirror')
        const bigImg = document.querySelector('.mirror img')
        // 绑定container的鼠标移动事件
        container.addEventListener('mousemove', e => {
            // 获取鼠标距离左侧和顶部的边界偏移值
            let x = e.clientX
            let y = e.clientY
            // 获取container距离左侧和顶部的边界偏移值
            let left = container.offsetLeft
            let Top = container.offsetTop
            // 获取放大镜（mirror）距离container的left和top，让放大镜居中鼠标
            let mirrorLeft = x - left - mirror.offsetWidth / 2
            let mirrorTop = y - Top - mirror.offsetHeight / 2

            mirror.style.left = mirrorLeft + 'px'
            mirror.style.top = mirrorTop + 'px'

            // 计算图片放大
            let bigImgLeft = (mirrorLeft + mirror.offsetWidth/2) / container.offsetWidth * bigImg.offsetWidth - mirror.offsetWidth / 2
            let bigImgTop = (mirrorTop + mirror.offsetHeight/2) / container.offsetHeight * bigImg.offsetHeight - mirror.offsetHeight / 2

            bigImg.style.left = -bigImgLeft + "px"
            bigImg.style.top = -bigImgTop + "px"
        })