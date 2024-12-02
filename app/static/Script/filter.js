
const filterButtons = document.querySelectorAll('.showContent');

const navbarItems = document.querySelectorAll('.navbar-nav li a');

   // بررسی کلیک روی هر دکمه فیلتر
   filterButtons.forEach(button => {
       button.addEventListener('click', () => {
           // استخراج پارامتر فیلتر از URL دکمه
           const filterParam = button.href.split('filter=')[1];
           // ذخیره پارامتر فیلتر در LocalStorage
           localStorage.setItem('activeFilter', filterParam);
       });
   });

   // بازیابی فیلتر فعال از LocalStorage
   const activeFilter = localStorage.getItem('activeFilter');

   // اگر فیلتر فعالی وجود داشت، آن را برجسته کن
   if (activeFilter) {
       filterButtons.forEach(button => {
           if (button.href.includes(`filter=${activeFilter}`)) {
               console.log('skjdffff')
               // اضافه کردن کلاس به دکمه فعال
               button.classList.add('bg-BlueC-300');
             
           } 
           else {
               // بازگرداندن کلاس‌های پیش‌فرض برای دکمه‌های غیر فعال
               button.classList.add('bg-BlueC-300');
               button.classList.remove('bg-BlueC-300');
           }
       });
   }



//    Menu

    

    // پیمایش از میان تمامی آیتم‌های نوبار
    navbarItems.forEach(item => {
        // بررسی کلیک روی آیتم نوبار
        item.addEventListener('click', () => {
            // ذخیره آدرس لینک کلیک شده در LocalStorage
            localStorage.setItem('activeNavLink', item.href);
        });
    });

    // بازیابی لینک فعال از LocalStorage
    const activeNavLink = localStorage.getItem('activeNavLink');

    // در صورت وجود لینک فعال، آن را برجسته کن
    if (activeNavLink) {
        navbarItems.forEach(item => {
            if (item.href === activeNavLink) {
                // اضافه کردن کلاس به آیتم فعال
                item.classList.add('text-BlueC-800');
            } else {
                // حذف کردن کلاس از آیتم‌های غیر فعال
                item.classList.remove('text-BlueC-800');
            }
        });
    }