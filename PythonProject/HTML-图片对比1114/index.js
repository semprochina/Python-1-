  const range = document.querySelector('input');
    const compare = document.querySelector('.compare'); // 获取容器元素

    range.oninput = function () {
        compare.style.setProperty('--pos', range.value + '%'); // 更新容器变量
    };