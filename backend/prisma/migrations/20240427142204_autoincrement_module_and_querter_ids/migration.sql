-- AlterTable
CREATE SEQUENCE module_id_seq;
ALTER TABLE "Module" ALTER COLUMN "id" SET DEFAULT nextval('module_id_seq');
ALTER SEQUENCE module_id_seq OWNED BY "Module"."id";

-- AlterTable
CREATE SEQUENCE quarter_id_seq;
ALTER TABLE "Quarter" ALTER COLUMN "id" SET DEFAULT nextval('quarter_id_seq');
ALTER SEQUENCE quarter_id_seq OWNED BY "Quarter"."id";
