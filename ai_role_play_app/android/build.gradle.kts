buildscript {
    repositories {
        // 暂时注释掉阿里云镜像（优先使用）
        // maven { url = uri("https://maven.aliyun.com/repository/google") }
        // maven { url = uri("https://maven.aliyun.com/repository/jcenter") }
        // maven { url = uri("https://maven.aliyun.com/repository/public") }
        // 保留原有的 google() 和 mavenCentral()（备用）
        google()
        mavenCentral()
    }
    // ... 其他代码（保持不变）
}

allprojects {
    repositories {
                // 暂时注释掉阿里云镜像（优先使用）
        // maven { url = uri("https://maven.aliyun.com/repository/google") }
        // maven { url = uri("https://maven.aliyun.com/repository/jcenter") }
        // maven { url = uri("https://maven.aliyun.com/repository/public") }
        // 保留原有的 google() 和 mavenCentral()（备用）
        google()
        mavenCentral()
    }
}

val newBuildDir: Directory =
    rootProject.layout.buildDirectory
        .dir("../../build")
        .get()
rootProject.layout.buildDirectory.value(newBuildDir)

subprojects {
    val newSubprojectBuildDir: Directory = newBuildDir.dir(project.name)
    project.layout.buildDirectory.value(newSubprojectBuildDir)
}
subprojects {
    project.evaluationDependsOn(":app")
}

tasks.register<Delete>("clean") {
    delete(rootProject.layout.buildDirectory)
}
