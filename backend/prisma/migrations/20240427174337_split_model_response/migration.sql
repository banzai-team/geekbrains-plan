-- CreateTable
CREATE TABLE "OutputClEduCourses" (
    "id" SERIAL NOT NULL,
    "response_id" INTEGER NOT NULL,
    "edu_course" INTEGER NOT NULL,

    CONSTRAINT "OutputClEduCourses_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "OutputClSimularCourse" (
    "id" SERIAL NOT NULL,
    "response_id" INTEGER NOT NULL,
    "match_score" DOUBLE PRECISION NOT NULL,
    "program_id" INTEGER NOT NULL,

    CONSTRAINT "OutputClSimularCourse_pkey" PRIMARY KEY ("id")
);
